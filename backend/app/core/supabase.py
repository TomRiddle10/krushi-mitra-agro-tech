from supabase import create_client, Client

from app.core.config import settings


if not settings.SUPABASE_URL:
    raise ValueError("SUPABASE_URL is not configured")

if not settings.SUPABASE_KEY:
    raise ValueError("SUPABASE_KEY is not configured")


supabase: Client = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_KEY
)