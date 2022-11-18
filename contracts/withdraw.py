#!/usr/bin/env python3


from pyteal import *
import os

def approval_program():

    withdraw_account_key = Bytes("withdraw_account")
    withdraw_time_key = Bytes("withdraw_time")

    on_create = Seq(
        Assert(Txn.application_args.length() == Int(1)),
        App.globalPut(withdraw_account_key, Txn.accounts[1]),
        App.globalPut(withdraw_time_key, Btoi(Txn.application_args[0])),
        Approve()
    )

    on_withdraw = Seq(
        # We check if the calling account is the account that is allowed to withdraw the Algos
        # and if the latest timestamp is larger than the withdraw start time
        Assert(And(
            Txn.sender() == App.globalGet(withdraw_account_key),
            Global.latest_timestamp() >= App.globalGet(withdraw_time_key),
            Txn.application_args.length() == Int(1),
        )),
        # In order to send the Algos to the calling account, we need to issue an inner payment transaction.
        # This can be done using the InnerTxnBuilder class.
        # We set the type of the inner transaction to payment. The amount field of the transaction is set
        # to the desired withdraw amount passed to the app call via the first argument. The receiver of the
        # payment is the withdraw account.
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields(
            {
                TxnField.type_enum: TxnType.Payment,
                TxnField.amount: Btoi(Txn.application_args[0]),
                TxnField.receiver: App.globalGet(withdraw_account_key)
            }
        ),
        InnerTxnBuilder.Submit(),
        Approve()
        )

    on_delete =  Seq(
        # Again, we check if the calling account is the account that is allowed to withdraw the Algos
        # and if the latest timestamp is larger than the withdraw start time
        Assert(And(
            Txn.sender() == App.globalGet(withdraw_account_key),
            Global.latest_timestamp() >= App.globalGet(withdraw_time_key),
        )),
        # Again we use an inner transaction to send the remaining balance to the withdraw account.
        # Algorand provides a special field in payment transactions (close_remainder_to) that can be
        # used to transfer the remaining account balance to a specific account when an account is deleted
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields(
            {
                TxnField.type_enum: TxnType.Payment,
                TxnField.close_remainder_to: App.globalGet(withdraw_account_key),
            }
        ),
        InnerTxnBuilder.Submit(),
        Approve()
        )

    return Cond(
        [Txn.application_id() == Int(0), on_create],
        [Txn.on_completion() == OnComplete.DeleteApplication, on_withdraw], # We handle deleting the app as withdrawing with subsequently deleting the app
        [Txn.on_completion() == OnComplete.UpdateApplication, Reject()], # Update app is not implemented
        [Txn.on_completion() == OnComplete.CloseOut, Reject()], # CloseOut is not implemented
        [Txn.on_completion() == OnComplete.OptIn, Reject()], # OptIn is not implemented
        [Txn.on_completion() == OnComplete.NoOp, on_withdraw], # Event handler
    )

# Clear state program does nothing since app does not use local state
def clear_state_program():
    return Approve()

# Compiles PyTEAL code to TEAL, .teal files are placed into ./build
if __name__ == "__main__":
    os.makedirs("build", exist_ok=True)
    approval_file = "build/withdraw_approval.teal"
    with open(approval_file, "w") as f:
        compiled = compileTeal(approval_program(), mode=Mode.Application, version=5)
        f.write(compiled)

    clear_state_file = "build/withdraw_clear_state.teal"
    with open(clear_state_file, "w") as f:
        compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=5)
        f.write(compiled)
