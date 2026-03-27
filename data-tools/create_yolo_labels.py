"""Convert VinDr train.csv annotations to YOLO label format (.txt files)."""

from pathlib import Path


# Class mapping from VinDr lesion names to YOLO class IDs
CLASS_MAP = {
    "No finding": 0,
    "Aortic enlargement": 1,
    "Atelectasis": 2,
    "Calcification": 3,
    "Cardiomegaly": 4,
    "Consolidation": 5,
    "ILD": 6,
    "Infiltration": 7,
    "Lung Opacity": 8,
    "Nodule/Mass": 9,
    "Other lesion": 10,
    "Pleural effusion": 11,
    "Pleural thickening": 12,
    "Pneumothorax": 13,
    "Pulmonary fibrosis": 14,
}


def convert_bbox_to_yolo(
    x_min: float,
    y_min: float,
    x_max: float,
    y_max: float,
    img_width: int,
    img_height: int,
) -> tuple[float, float, float, float]:
    """Convert absolute [x_min, y_min, x_max, y_max] to YOLO [cx, cy, w, h] normalized."""
    cx = (x_min + x_max) / 2 / img_width
    cy = (y_min + y_max) / 2 / img_height
    w = (x_max - x_min) / img_width
    h = (y_max - y_min) / img_height
    return cx, cy, w, h


def main() -> None:
    csv_path = Path("data/raw/train.csv")
    images_dir = Path("data/yolo_dataset/images")
    labels_dir = Path("data/yolo_dataset/labels")

    labels_dir.mkdir(parents=True, exist_ok=True)

    print(f"TODO: read {csv_path}, convert bboxes, write YOLO .txt to {labels_dir}")
    print(f"      Images expected in {images_dir}")
    print(f"      Class map: {CLASS_MAP}")


if __name__ == "__main__":
    main()
