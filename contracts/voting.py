#!/usr/bin/env python3
from pyteal import *
import os

# Keys
# We define the keys outside of the context op approval_program since we need them in clear_state_program as well
registration_begin = Bytes("reg_bgn")
registration_end = Bytes("reg_end")
vote_begin = Bytes("vote_bgn")
vote_end = Bytes("vote_end")
vote_count_yes = Bytes("votes_yes")
vote_count_no = Bytes("votes_no")
has_voted = Bytes("has_voted")

# Op messages
yes_vote = Bytes("yes")
no_vote = Bytes("no")

def approval_program():

    on_creation = Seq(
            Assert(Txn.application_args.length() == Int(4)),
            App.globalPut(registration_begin, Btoi(Txn.application_args[0])),
            App.globalPut(registration_end, Btoi(Txn.application_args[1])),
            App.globalPut(vote_begin, Btoi(Txn.application_args[2])),
            App.globalPut(vote_end, Btoi(Txn.application_args[3])),
            App.globalPut(vote_count_yes, Int(0)),
            App.globalPut(vote_count_no, Int(0)),
            Approve(),
    )

    # We use the optin call for registration
    # We allow to optin during registration period, note that And returns either 1 or 0, therefore we don't need Approve() or Reject()
    on_optin = Return(
        And(
            Global.round() >= App.globalGet(registration_begin),
            Global.round() <= App.globalGet(registration_end)
        )
    )

    get_sender_vote = App.localGetEx(Txn.sender(), App.id(), has_voted)

    on_vote = Seq(
        # Note that all calls to local state for this app will fail if the sender account has not opted in, i.e. if i has not registered
        # Check if still within voting period
        Assert(And(
            Global.round() >= App.globalGet(vote_begin),
            Global.round() <= App.globalGet(vote_end)
        )),
        # Check if account already has voted
        # Note: get_sender_vote has to be called before hasValue() can be used on it. This is required by Appl.localGetEx
        get_sender_vote,
        Assert(Not(get_sender_vote.hasValue())),

        # Update vote counter based on vote
        Cond(
            [Txn.application_args[0] == yes_vote, App.globalPut(vote_count_yes, App.globalGet(vote_count_yes) + Int(1))],
            [Txn.application_args[0] == no_vote, App.globalPut(vote_count_no, App.globalGet(vote_count_no) + Int(1))]
        ),
        # Set the has_voted field to the sender's vote, to make sure an account cannot vote again
        App.localPut(Txn.sender(), has_voted, Txn.application_args[0]),
        Approve()
    )
    # We use the close out call to retract an accounts vote
    # This is only possible during the voting period, afterwards the accounts vote is immutable
    on_close_out =  Seq(
            Assert(Global.round() <= App.globalGet(vote_end)),
            get_sender_vote,
            Cond(
                [get_sender_vote.value() == yes_vote, App.globalPut(vote_count_yes, App.globalGet(vote_count_yes) - Int(1))],
                [get_sender_vote.value() == no_vote, App.globalPut(vote_count_no, App.globalGet(vote_count_no) - Int(1))]
            ),
            Approve()
    )


    return Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.DeleteApplication, Approve()],
        [Txn.on_completion() == OnComplete.UpdateApplication, Reject()],
        [Txn.on_completion() == OnComplete.CloseOut, on_close_out],
        [Txn.on_completion() == OnComplete.OptIn, on_optin],
        [Txn.on_completion() == OnComplete.NoOp, on_vote],
    )


# The clear state program can also be used to retract an accounts vote. The logic is the same as for the close out call.
def clear_state_program():
    get_sender_vote = App.localGetEx(Txn.sender(), App.id(), has_voted)

    return Seq(
            Assert(Global.round() <= App.globalGet(vote_end)),
            get_sender_vote,
            Cond(
                [get_sender_vote.value() == yes_vote, App.globalPut(vote_count_yes, App.globalGet(vote_count_yes) - Int(1))],
                [get_sender_vote.value() == no_vote, App.globalPut(vote_count_no, App.globalGet(vote_count_no) - Int(1))]
            ),
            Approve()
    )




# Compiles PyTEAL code to TEAL, .teal files are placed into ./build
if __name__ == "__main__":
    os.makedirs("build", exist_ok=True)
    approval_file = "build/voting_approval.teal"
    with open(approval_file, "w") as f:
        compiled = compileTeal(approval_program(), mode=Mode.Application, version=5)
        f.write(compiled)

    clear_state_file = "build/voting_clear_state.teal"
    with open(clear_state_file, "w") as f:
        compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=5)
        f.write(compiled)
