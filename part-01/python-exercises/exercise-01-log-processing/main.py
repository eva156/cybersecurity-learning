
"""
Exercise 1: Log Processing

Process a list of usernames to identify unique users 
and calculate login statistics.
"""

def get_sample_data() -> list[str]:
    """Returns a sample list of usernames from authentication logs."""
    usernames = [" alice","bob","alice","charlie","bob","alice","david"]

    return usernames


def get_unique_usernames(usernames: list[str]) -> set[str]:
    """Return a set containing only unique usernames."""    
    unique_users = {u.strip() for u in usernames}
    unique_users.discard("")
    
    return set(sorted(unique_users))


def get_login_statistics(usernames: list[str]) -> dict[str, int]:
    """Returns the total login attempts and number of unique users."""
    # Login attempts: every recorded event (including empty usernames)
    login_attempts = len(usernames)
    # Unique users: every valid, distinct username
    num_users = len(get_unique_usernames(usernames))
    user_stats = {"total_attempts": login_attempts, "unique_users": num_users}

    return user_stats


def display_results(
    unique_usernames: set[str],
    statistics: dict[str, int]
) -> None:
    """Display the login analysis results."""
    print(f"Total login attempts: {statistics['total_attempts']}")
    print(f"Unique users: {statistics['unique_users']}")
    print(f"Unique usernames: {unique_usernames}")


# 5. Main execution
def main() -> None:
    """Run the log processing exercise."""
    usernames = get_sample_data()
    unique_usernames = get_unique_usernames(usernames)
    stats = get_login_statistics(usernames)
    display_results(unique_usernames, stats)


if __name__ == "__main__":
    main()
