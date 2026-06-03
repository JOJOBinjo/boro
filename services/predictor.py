import numpy as np
from services.model_loader import load_model

CLASSES = [
    "барокко",
    "ренесанс",
    "рококо",
    "классицизм",
    "не барокко"
]

def preprocess(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))

    img = np.array(image).astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    return img


def predict_style(image):
    model = load_model()

    img = preprocess(image)

    probs = model.predict(img, verbose=0)[0]

    idx = int(np.argmax(probs))
    confidence = float(probs[idx] * 100)

    # формируем красивый словарь всех вероятностей
    all_probs = {
        CLASSES[i]: float(probs[i] * 100)
        for i in range(len(CLASSES))
    }

    return {
        "label": CLASSES[idx],
        "confidence": round(confidence, 2),
        "all_probs": all_probs
    }