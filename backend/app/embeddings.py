import logging
from typing import Optional
from functools import cache

import cohere

from app.config import settings
from app.custom_types import Embedding

_logger = logging.getLogger(__name__)


@cache
def get_cohere_client() -> cohere.Client:
    return cohere.ClientV2(settings.cohere_api_key)
    

def get_embeddings(text: str) -> Optional[Embedding]:
    try:
        response = get_cohere_client().embed(
            texts=[text],
            input_type="search_query", 
            embedding_types=["float"],
            model="embed-english-v3.0",
            truncate="END"
        )
        return response.embeddings.float_[0]
    except Exception as e:
        _logger.error(f"Error getting embedding: {e}")
