"""
Local stub for sslcommerz_lib so the project can run in local development
without the real SSLCommerz gateway.

This does NOT perform real payments. It only prevents import errors.
"""

class SSLCOMMERZ:
    def __init__(self, settings):
        """
        settings: dict with keys like store_id, store_pass, issandbox, etc.
        We just store them; no real API calls are made.
        """
        self.settings = settings

    def createSession(self, post_body):
        """
        In the real library, this would create a payment session
        and return a dict containing 'GatewayPageURL'.
        Here we return a fake response.
        """
        return {
            "status": "STUB",
            "GatewayPageURL": "#",  # no real redirect
            "message": "SSLCOMMERZ stub in local dev – no real payment created.",
            "post_body": post_body,
        }

    def hash_validate_ipn(self, post_body):
        """
        In real life, validates IPN hash from SSLCommerz.
        Here we just pretend it's always valid.
        """
        return True

    def validationTransactionOrder(self, val_id):
        """
        In real life, validates a transaction.
        Here we just return a stub dict.
        """
        return {
            "status": "STUB",
            "val_id": val_id,
            "message": "Validation stubbed in local dev.",
        }

    def transaction_query_session(self, sessionkey):
        return {
            "status": "STUB",
            "sessionkey": sessionkey,
            "message": "Session query stubbed in local dev.",
        }

    def transaction_query_tranid(self, tranid):
        return {
            "status": "STUB",
            "tranid": tranid,
            "message": "TranID query stubbed in local dev.",
        }

    def init_refund(self, bank_tran_id, refund_amount, refund_remarks):
        return {
            "status": "STUB",
            "bank_tran_id": bank_tran_id,
            "refund_amount": refund_amount,
            "refund_remarks": refund_remarks,
            "refund_ref_id": "stub-ref-id",
            "message": "Refund init stubbed in local dev.",
        }

    def query_refund_status(self, refund_ref_id):
        return {
            "status": "STUB",
            "refund_ref_id": refund_ref_id,
            "message": "Refund status stubbed in local dev.",
        }
