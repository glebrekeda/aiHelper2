import yadisk
import secrets

appId = secrets.yad_appId
appSecret = secrets.yad_appSecret
token = secrets.yad_token
client = yadisk.Client(appId, appSecret, token)

# Вы можете использовать либо конструкцию with, либо вручную вызвать client.close() в конце
with client:
    print('client')
    # Проверяет, валиден ли токен
    print(client.check_token())

    # Получает общую информацию о диске
    #print(client.get_disk_info())

    # Выводит содержимое "/some/path"
    #print(list(client.listdir("/Загрузки")))

    # Загружает "file_to_upload.txt" в "/destination.txt"
    #client.upload("file_to_upload.txt", "/destination.txt")

    # То же самое
    #with open("file_to_upload.txt", "rb") as f:
    #    client.upload(f, "/destination.txt")

    # Скачивает "/some-file-to-download.txt" в "downloaded.txt"
    client.download("/Загрузки/testfile.docx", "wrk/testfile.docx")

    # Безвозвратно удаляет "/file-to-remove"
    #client.remove("/file-to-remove", permanently=True)

    # Создаёт новую папку "/test-dir"
    #print(client.mkdir("/test-dir"))