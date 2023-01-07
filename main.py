import json
from login import login
from config import USERNAME,IDENTITY


class Calculator:
    def __init__(self):
        self.identity = IDENTITY
        self.login()
        self.student_ID = self.get_student_ID()
        self.course_select_turn_ID = self.get_course_select_turn_ID()
        self.addable_lessons = self.get_addable_lessons()

    def login(self):
        if self.identity == 'undergraduate':
            service_url = 'https://jw.ustc.edu.cn/ucas-sso/login'
        elif self.identity == 'postgraduate':
            service_url = 'https://yjs.ustc.edu.cn/default.asp'
        else:
            raise ValueError
        self.session = login(service_url)

    def get_student_ID(self):
        if self.identity == 'undergraduate':
            url = 'https://jw.ustc.edu.cn/for-std/course-select'
        elif self.identity == 'postgraduate':
            ASPSESSIONID_KEY, ASPSESSIONID_VALUE = list(
                self.session.cookies.get_dict('yjs.ustc.edu.cn').items())[0]
            url = f'https://jw.ustc.edu.cn/graduate-login?stn={USERNAME}&{ASPSESSIONID_KEY}={ASPSESSIONID_VALUE}'
        else:
            raise ValueError
        r = self.session.get(url)
        return r.url.split('/')[-1]

    def get_course_select_turn_ID(self):
        if self.identity == 'undergraduate':
            bizTypeId = '2'
        elif self.identity == 'postgraduate':
            bizTypeId = '3'
        else:
            raise ValueError
        data = {
            'bizTypeId': bizTypeId,
            'studentId': self.student_ID,
        }
        url = 'https://jw.ustc.edu.cn/ws/for-std/course-select/open-turns'
        r = self.session.post(url, data=data)
        r = json.loads(r.text)
        assert len(r) == 1
        return r[0]['id']

    def get_addable_lessons(self):
        url = 'https://jw.ustc.edu.cn/ws/for-std/course-select/addable-lessons'
        data = {
            'turnId': self.course_select_turn_ID,
            'studentId': self.student_ID
        }
        r = self.session.post(url, data=data)
        return json.loads(r.text)

    def get_selected_lessons(self):
        url = 'https://jw.ustc.edu.cn/ws/for-std/course-select/selected-lessons'
        data = {
            'turnId': self.course_select_turn_ID,
            'studentId': self.student_ID
        }
        r = self.session.post(url, data=data)
        return json.loads(r.text)


if __name__ == '__main__':
    calc = Calculator()
    get = calc.get_selected_lessons()
    total_credits = 0

    print('学号: ' + USERNAME + '\n已选择课程:')

    for course in get:
        print(str(course['course']['credits']) + " - " + course['course']['nameZh'] )
        total_credits += course['course']['credits']

    print('总学分: ' + str(total_credits) + '\n')