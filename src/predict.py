def predict_from_input(model, symptom_columns):
    print("\n🧪 Enter symptoms (1 = yes, 0 = no):")
    user_input = []
    for symptom in symptom_columns:
        val = input(f"{symptom}: ")
        user_input.append(int(val))
    prediction = model.predict([user_input])
    print(f"\n🩺 Predicted Disease: {prediction[0]}")
