"""Remove sensitive metadata from medical imaging files."""

from pathlib import Path


def main() -> None:
    input_dir = Path("./input")
    output_dir = Path("./anonymized")
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"TODO: anonymize data from {input_dir} into {output_dir}")


if __name__ == "__main__":
    main()
