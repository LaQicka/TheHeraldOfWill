# import gpt4free.g4f as g4f
import g4f
import requests


def check_proxy(proxy_url):
    try:
        # Установите прокси
        proxies = {
            'http': proxy_url,
            'https': proxy_url
        }

        # Отправьте запрос через прокси
        response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
        
        # Проверьте статус ответа
        if response.status_code == 200:
            print(f"Прокси работает: {response.text}")
        else:
            print(f"Прокси вернул статус: {response.status_code}")
        
    except requests.exceptions.ProxyError:
        print("Ошибка прокси: Не удалось установить соединение.")
    except requests.exceptions.ConnectTimeout:
        print("Ошибка прокси: Превышено время ожидания соединения.")
    except requests.exceptions.SSLError:
        print("Ошибка прокси: Проблема SSL соединения.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка прокси: {e}")

def ask_gpt_3_5_turbo(prompt):
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    )
    return response

# def ask_gpt_4(messages: list) -> str:
#     response = g4f.ChatCompletion.create(
#     model="gpt-4",
#     messages=messages,
#     )
#     return response

def ask_gpt_4(prompt):
    response = g4f.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    )
    return response

if __name__ == "__main__":
    pass