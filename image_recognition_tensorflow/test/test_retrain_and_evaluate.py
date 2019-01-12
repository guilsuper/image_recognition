#!/usr/bin/env python
import os

import rospkg
from image_recognition_tensorflow.evaluate_classifier import evaluate_classifier
from image_recognition_tensorflow.retrain import defaults, main


def test_retrain_and_evaluate():
    pkg_path = rospkg.RosPack().get_path("image_recognition_tensorflow")
    models_path = os.path.join(pkg_path, 'test/models')
    assets_path = os.path.join(pkg_path, 'test/assets')

    main(os.path.join(assets_path, "training"), models_path, models_path, defaults.steps, defaults.batch)
    accuracy = evaluate_classifier(os.path.join(models_path, "output_graph.pb"),
                                   os.path.join(models_path, "output_labels.txt"),
                                   os.path.join(assets_path, "verification"), "result.csv")
    assert accuracy > 0.5
