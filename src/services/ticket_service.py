from __future__ import annotations

from src.config import TICKET_DB
from src.utils.sqlite_loader import get_connection


class TicketService:
    """
    Business logic for Support Ticket operations.
    """

    def __init__(self) -> None:
        self.db_path = TICKET_DB

    def search_tickets(
        self,
        service_name: str | None = None,
        status: str | None = None,
    ) -> list[dict]:
        """
        Search tickets using optional filters.
        """

        conn = get_connection(self.db_path)
        cursor = conn.cursor()

        query = "SELECT * FROM tickets WHERE 1=1"
        params = []

        if service_name:
            query += " AND service_name = ?"
            params.append(service_name)

        if status:
            query += " AND status = ?"
            params.append(status)

        cursor.execute(query, params)

        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]

    def get_ticket_details(self, ticket_id: str) -> dict:
        """
        Return details for a ticket.
        """

        conn = get_connection(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tickets WHERE ticket_id = ?",
            (ticket_id,),
        )

        row = cursor.fetchone()

        conn.close()

        if row is None:
            return {
                "found": False,
                "message": f"{ticket_id} not found.",
            }

        return {
            "found": True,
            **dict(row),
        }

    def get_high_priority_tickets(self) -> list[dict]:
        """
        Return OPEN P1/P2 tickets.
        """

        conn = get_connection(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM tickets
            WHERE status='OPEN'
            AND priority IN ('P1','P2')
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]