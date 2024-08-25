from langchain_chroma import Chroma
from langchain.embeddings.base import Embeddings
from langchain.schema import BaseRetriever

class RedundantFilterRetriver(BaseRetriever):
    embeddings: Embeddings
    chroma: Chroma
    def get_relevant_documents(self, query: str):
        # Get the embeddings for the query
        emb = self.embeddings.embed_query(query)
        # take embeddings and feed them into that
        # max_marginal_relevance_search_by_vector
        return self.chroma.amax_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8
        )
    
    async def _aget_relevant_documents(self):
        return []