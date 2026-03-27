"""Ingest embeddings or metadata into Pinecone."""

from pathlib import Path


def main() -> None:
    source_dir = Path("./prepared_vectors")
    print(f"TODO: ingest vectors from {source_dir} to Pinecone")


if __name__ == "__main__":
    main()
