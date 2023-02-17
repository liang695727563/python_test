# -*- coding: UTF-8 -*-
#coding=utf-8

list1 = ['physics','chemistry',1997,2000];
list2 = [1, 2, 3, 4, 5, 6, 7];
list3 = ["a", 'b', "c", "d"];

print list1,list2,list3

print "list1[0]:",list1[0]
print "list2[1:5]:", list2[1:5]
print "list2[2:]:", list2[2:]
print 'list2[2:4]:', list2[2:4]
print "list2[2:3]:", list2[2:3]
print 'list2[:3]:', list2[:3];






list = ['physics', 'chemistry', 1997, 2000]

print "Value available at index 2 :"
print list[2];
list[2] = 2001;
print "New value available at index 2 :"
print list[2];

# É¾³ıÁĞ±íÔªËØ -- del Óï¾ä
list1 = ['physics', 'chemistry', 1997, 2000] 
print list1
del list1[2];
print "After deleting value at index 2 :"
print list1;
