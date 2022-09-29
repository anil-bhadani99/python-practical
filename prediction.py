import requests
import json


class PredictionView():
    try:
        result = []
        for k in [{"name": "Ash"}, {'name': 'Misty'}, {'name': 'Brock'}]:
            user_details = requests.get(
                url="https://api.agify.io", params=k).json()
            user_gender = requests.get(
                url="https://api.genderize.io", params=k).json()
            user_location = requests.get(
                url="https://api.nationalize.io", params=k).json()

            # Extra api call for Bonus task
            user_dummy_data = requests.get(
                url="https://randomuser.me/api/").json()['results'][0]
            country_sort = max(
                user_location["country"], key=lambda x: x['probability'])
            del user_gender["name"], user_gender["count"], user_gender["probability"], user_dummy_data[
                "login"], user_dummy_data["dob"], user_dummy_data["registered"], user_dummy_data["name"], user_dummy_data["gender"], user_dummy_data["id"], user_dummy_data["nat"]

            result.append({**country_sort, **user_gender, **
                          user_details, **user_dummy_data})

        main_dict = {"Count": len(result), "person": result}
        with open('output.json', 'w') as outfile:
            json.dump(main_dict, outfile, indent=4)
        print("File created successfully")
    except Exception as e:
        print(e)
