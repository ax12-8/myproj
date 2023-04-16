#include <exception>
using namespace std;

#ifndef __student_info_h__
#define __student_info_h__

// #include "administrator.h"
// #include "logonui.h"
#include "teacher.h"

class administrator;
class logonui;
class teacher;
class student_info;

class student_info
{
	public: int _stunumber;
	public: VARCHAR _name;
	public: int _roomnum;
	public: VARCHAR _major;
	public: administrator* _generate;
	public: logonui* _display;
	public: teacher** _maintain;

	public: void record_student_info();

	public: void update_student_info();

	public: void delete_info();

	public: void load_info();

	private: void saveinfo();
};

#endif
