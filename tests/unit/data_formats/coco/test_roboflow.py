# Copyright (C) 2023 Intel Corporation
#
# SPDX-License-Identifier: MIT

import numpy as np
import pytest

from datumaro.components.annotation import Bbox, Mask, Polygon
from datumaro.components.dataset import Dataset
from datumaro.components.dataset_base import DatasetItem
from datumaro.components.media import Image
from datumaro.plugins.data_formats.coco.importer import CocoRoboflowImporter

from ..base import TestDataFormatBase

from tests.utils.assets import get_test_asset_path

STRICT_DIR = get_test_asset_path("coco_dataset", "yolo")


class CocoRoboflowTest(TestDataFormatBase):
    IMPORTER = CocoRoboflowImporter
    USE_TEST_CAN_EXPORT_AND_IMPORT = False

    @pytest.fixture()
    def fxt_dataset_dir(self) -> str:
        return get_test_asset_path("coco_dataset", "coco_roboflow")

    @pytest.fixture()
    def fxt_expected_dataset(self) -> Dataset:
        return Dataset.from_iterable(
            [
                DatasetItem(
                    id="a",
                    subset="train",
                    media=Image.from_numpy(data=np.ones((5, 10, 3))),
                    attributes={"id": 5},
                    annotations=[
                        Bbox(2, 2, 3, 1, label=1, group=1, id=1, attributes={"is_crowd": False})
                    ],
                ),
                DatasetItem(
                    id="b",
                    subset="val",
                    media=Image.from_numpy(data=np.ones((10, 5, 3))),
                    attributes={"id": 40},
                    annotations=[
                        Polygon(
                            [0, 0, 1, 0, 1, 2, 0, 2],
                            label=0,
                            id=1,
                            group=1,
                            attributes={"is_crowd": False, "x": 1, "y": "hello"},
                        ),
                        Bbox(
                            0.0,
                            0.0,
                            1.0,
                            2.0,
                            id=1,
                            attributes={"x": 1, "y": "hello", "is_crowd": False},
                            group=1,
                            label=0,
                            z_order=0,
                        ),
                        Mask(
                            np.array([[1, 1, 0, 0, 0]] * 10),
                            label=1,
                            id=2,
                            group=2,
                            attributes={"is_crowd": True},
                        ),
                        Bbox(
                            0.0,
                            0.0,
                            1.0,
                            9.0,
                            id=2,
                            attributes={"is_crowd": True},
                            group=2,
                            label=1,
                            z_order=0,
                        ),
                    ],
                ),
            ],
            categories=["a", "b", "c"],
        )
