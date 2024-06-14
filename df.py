from deepface import DeepFace

face_detection_model = "retinaface"
face_recognition_model = "Facenet"


def verify(img_1, img_2):
    return DeepFace.verify(
        img1_path=img_1,
        img2_path=img_2,
        model_name=face_recognition_model,
        detector_backend=face_detection_model,
        distance_metric="cosine"
    )
