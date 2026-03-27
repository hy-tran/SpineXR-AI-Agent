"""Convert DICOM files to JPG images."""

from pathlib import Path


def main() -> None:
    input_dir = Path("./input_dicom")
    output_dir = Path("./output_jpg")
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"TODO: convert DICOM from {input_dir} to JPG in {output_dir}")


if __name__ == "__main__":
    main()
