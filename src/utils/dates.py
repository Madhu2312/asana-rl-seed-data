import random
from datetime import datetime, timedelta
import numpy as np

# -----------------------------------
# GLOBAL TIME CONFIG
# -----------------------------------

NOW = datetime.now()
HISTORY_DAYS = 180

# -----------------------------------
# HELPER FUNCTIONS
# -----------------------------------

def random_past_datetime():
    """
    Generate a realistic creation timestamp within company history.
    Bias towards weekdays and earlier in the week.
    """
    days_ago = random.randint(0, HISTORY_DAYS)
    base_date = NOW - timedelta(days=days_ago)

    # Bias toward working hours
    hour = random.choice(range(9, 18))
    minute = random.choice(range(0, 60))

    return base_date.replace(hour=hour, minute=minute, second=0, microsecond=0)


def generate_due_date(created_at):
    """
    Generate due dates with realistic planning horizons.
    """
    roll = random.random()

    # 10% → no due date
    if roll < 0.10:
        return None

    # Short-term (within 7 days)
    if roll < 0.35:
        delta = random.randint(1, 7)

    # Medium-term (within 30 days)
    elif roll < 0.75:
        delta = random.randint(8, 30)

    # Long-term
    else:
        delta = random.randint(31, 90)

    due_date = created_at + timedelta(days=delta)

    # Avoid weekends 85% of time
    if random.random() < 0.85:
        while due_date.weekday() >= 5:
            due_date += timedelta(days=1)

    return due_date.date()


def generate_completion_timestamp(created_at, due_date=None):
    """
    Generate realistic completion times.
    Ensures logical ordering and occasional overdue completion.
    """
    # 15% chance task is still incomplete
    if random.random() < 0.15:
        return None

    # Completion typically 1–14 days after creation
    days_to_complete = int(np.random.lognormal(mean=2.0, sigma=0.5))
    completed_at = created_at + timedelta(days=days_to_complete)

    # Allow slight overdue completion
    if due_date and completed_at.date() < due_date:
        return completed_at

    return completed_at if completed_at < NOW else None
