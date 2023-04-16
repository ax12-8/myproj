#include <exception>
using namespace std;

#ifndef __logonui_h__
#define __logonui_h__

#include "student.h"
#include "student_info.h"

class student;
class student_info;
class logonui;

class logonui
{
	public: student** _use;
	public: student_info** _display;

	public: void logon();

	public: void view();
};

#endif
