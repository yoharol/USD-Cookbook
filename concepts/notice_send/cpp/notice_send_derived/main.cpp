// IMPORT THIRD-PARTY LIBRARIES
#include "pxr/base/tf/notice.h"


class NoticeBase : pxr::TfNotice {
};

class NoticeDerived : NoticeBase {};


class Callback : public pxr::TfWeakBase {
    public:
        Callback (int identity, pxr::TfNotice const &notice) : identity(identity), notice(notice) {}
        Callback (int identity, NoticeBase const &notice) : identity(identity), notice(notice) {}

        void ProcessNotice(
            pxr::TfNotice &notice,
            pxr::TfWeakPtr<Callback> const &sender
        ) {
            std::cout << "Got sender? " << (sender->identity == this->identity) << '\n';
            this->counter += 1;
        }

        int counter = 0;

    private:
        int identity;
        NoticeBase notice;
};


int main() {
    pxr::TfType::Define<NoticeBase, pxr::TfType::Bases<pxr::TfNotice> >();
    pxr::TfType::Define<NoticeDerived, pxr::TfType::Bases<pxr::TfNotice> >();

    auto notice = NoticeBase {};
    auto callback1 = new Callback {1, notice};
    pxr::TfWeakPtr<Callback> sender {callback1};
    auto key = pxr::TfNotice::Register(NoticeBase {}, &Callback::ProcessNotice, sender);

    auto callback2 = new Callback {2, notice};
    pxr::TfWeakPtr<Callback> sender2 {callback2};
    pxr::TfNotice::Register(NoticeDerived {}, &Callback::ProcessNotice, sender2);

    std::cout << "Custom count " << callback1->counter << '\n';

    // Note, the sender actually matters here. It has to be whatever was
    // provided to `Tf.Notice.Register`. Otherwise, the `callback1` method
    // will never be run.
    //
    notice.Send(sender);
    notice.Send(sender2);

    pxr::TfNotice::Revoke(key);
    notice.Send(sender);

    std::cout << "Custom count " << callback1->counter << '\n';

    // pointer clean-up // TODO: replace with unique_ptr?
    delete callback1;
    callback1 = nullptr;
    delete callback2;
    callback2 = nullptr;

    return 0;
}