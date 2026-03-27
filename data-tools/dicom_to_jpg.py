"""Convert DICOM files to JPG images."""

from pathlib import Path


def main() -> None:
    input_dir = Path("data/raw/train_images")
    output_dir = Path("data/yolo_dataset/images")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"TODO: convert DICOM from {input_dir} to JPG in {output_dir}")


if __name__ == "__main__":
    main()
