# Дипломная работа профессии «Python-разработчик с нуля»

## Backend приложения для социальной сети для обмена фотографиями с возможностью комментировать и ставить лайки.

### Описание задания:

Необходимо разработать backend приложения для социальной сети для обмена фотографиями. Прототип фронтенда приложения на скрине:

![](https://github.com/netology-code/spd-diplom/blob/main/Design.png)

---

**Описание выполненной работы:**

**Система реализована на Django, в качестве СУБД использован postgresql**

**Созданы необходимые модели и сериализаторы. Посты состоят из текста и фотографии, сохраняется время создания поста. Комментарий состоит из текста и даты его публикации. Комментарии могут быть написаны к определённой публикации**

**Помимо комментариев, пользователи также могут оставлять реакцию на публикацию в виде лайка. Реализована проверка на уникальность лайков.**

**При получении деталей публикации помимо полей самой публикации отображается список комментариев и количество лайков к публикации.**

**Реализована авторизация и аутентификациия по токену: публикации и комментарии могут создаваться только авторизованными пользователями, редактировать публикацию может только её автор.**
