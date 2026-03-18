#!/usr/bin/env python3
"""Test script to verify Zendesk connection"""

import os
from dotenv import load_dotenv
from zenpy import Zenpy

load_dotenv()

# Initialize Zendesk client
client = Zenpy(
    subdomain=os.getenv('ZENDESK_SUBDOMAIN'),
    email=os.getenv('ZENDESK_EMAIL'),
    token=os.getenv('ZENDESK_API_KEY')
)

print(f"Connecting to: {os.getenv('ZENDESK_SUBDOMAIN')}.zendesk.com")
print(f"Using email: {os.getenv('ZENDESK_EMAIL')}")
print("=" * 80)

# Fetch tickets
print("\nFetching latest tickets...")
tickets = list(client.tickets())[:5]

print(f"\nFound {len(tickets)} tickets:\n")
for ticket in tickets:
    print(f"Ticket #{ticket.id}")
    print(f"  Subject: {ticket.subject}")
    print(f"  Status: {ticket.status}")
    print(f"  Priority: {ticket.priority}")
    print(f"  Created: {ticket.created_at}")
    print(f"  Updated: {ticket.updated_at}")
    print()

