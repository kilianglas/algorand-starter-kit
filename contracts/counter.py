#!/usr/bin/env python3
from pyteal import *
import os

# Keys for the global key-value state of the smart contract
# Convenient to define keys here s.t. they can be reused when needed
owner_key = Bytes("owner")
counter_key = Bytes("counter")

# Operation messages
inc_op = Bytes("inc")
dec_op = Bytes("dec")

def approval_program():
    # Initialization
    on_creation = Seq(
        # Set owner to sender of initial tx
        App.globalPut(owner_key, Txn.sender()),
        # Initialize counter to 0
        App.globalPut(counter_key, Int(0)),
        # Same as Return(Int(1)), convenient to use this
        Approve()
    )

    # NoOp call
    # Implements counter logic
    # Can either be increment or decrement call, specified by first tx argument
    # Note that we do not check for the sender id here -> Anyone can increment or decrement the counter
    on_counter_event = Cond(
        # Called when op message is dec
        [Txn.application_args[0] == dec_op, Seq(
            # Decrement the counter
            App.globalPut(counter_key, App.globalGet(counter_key) - Int(1)),
            Approve()
        )],
        # Called when op message is inc
        [Txn.application_args[0] == inc_op, Seq(
            # Increment the counter
            App.globalPut(counter_key, App.globalGet(counter_key) - Int(1)),
            Approve()
        )]
    )

    # Only the owner should be allowed to delete the application
    on_delete_app = Cond(
        [Txn.sender() == App.globalGet(owner_key), Approve()]
    )

    return Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.DeleteApplication, on_delete_app],
        [Txn.on_completion() == OnComplete.UpdateApplication, Reject()], # Update app is not implemented
        [Txn.on_completion() == OnComplete.CloseOut, Reject()], # CloseOut is not implemented
        [Txn.on_completion() == OnComplete.OptIn, Reject()], # CloseOut is not implemented
        [Txn.on_completion() == OnComplete.NoOp, on_counter_event], # Event handler
    )

# Clear state program always succeeds and does nothing else
def clear_state_program():
    return Approve()

# Compiles PyTEAL code to TEAL, teal files are placed into ./build
if __name__ == "__main__":
    os.makedirs("build", exist_ok=True)
    approval_file = "build/counter_approval.teal"
    with open(approval_file, "w") as f:
        compiled = compileTeal(approval_program(), mode=Mode.Application, version=7)
        f.write(compiled)

    clear_state_file = "build/counter_clear_state.teal"
    with open(clear_state_file, "w") as f:
        compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=7)
        f.write(compiled)
