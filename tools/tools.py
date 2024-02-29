from langchain_community.utilities.serpapi import SerpAPIWrapper


def get_profile_url(text: str) -> str:
    """Searches for Linkedin or twitter Profile Page."""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
