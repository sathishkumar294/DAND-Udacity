#!/usr/bin/env python
from datetime import datetime as dt
import unicodecsv


def read_csv(filename):
    """ Function to read a CSV file and return the list of records as JSON"""
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)


def parse_date(sdate):
    """Function converts string to date"""
    if sdate == '':
        return None
    else:
        return dt.strptime(sdate, '%Y-%m-%d')


def parse_int(sint):
    """Function to convert string to int"""
    if sint == '':
        return None
    else:
        return int(sint)


def parse_float_int(sfloat):
    """ Function to convert a float string to int """
    if sfloat == '':
        return None
    else:
        return int(float(sfloat))


def parse_float(sfloat):
    if sfloat == '':
        return None
    else:
        return float(sfloat)


print 'Parsing enrollments...'
enrollments = read_csv('enrollments.csv')
print 'Parsing engagements...'
daily_engagement = read_csv('daily_engagement.csv')
print 'Parsing submissions...'
project_submissions = read_csv('project_submissions.csv')

print 'Post processing enrollments...'
enrollment_students = set()
for enrolement in enrollments:
    enrolement['account_key'] = parse_int(enrolement['account_key'])
    enrolement['join_date'] = parse_date(enrolement['join_date'])
    enrolement['cancel_date'] = parse_date(enrolement['cancel_date'])
    enrolement['days_to_cancel'] = parse_int(enrolement['days_to_cancel'])
    enrolement['is_udacity'] = enrolement['is_udacity'] == 'True'
    enrolement['is_canceled'] = enrolement['is_canceled'] == 'True'
    enrollment_students.add(enrolement['account_key'])


print 'Post processing engagements...'
engagement_students = set()
for engagement in daily_engagement:
    engagement['acct'] = parse_int(engagement['acct'])
    engagement['utc_date'] = parse_date(engagement['utc_date'])
    engagement['num_courses_visited'] = parse_float_int(
        engagement['num_courses_visited'])
    engagement['total_minutes_visited'] = parse_float(
        engagement['total_minutes_visited'])
    engagement['lessons_completed'] = parse_float_int(
        engagement['lessons_completed'])
    engagement['projects_completed'] = parse_float_int(
        engagement['projects_completed'])
    engagement_students.add(engagement['acct'])

print 'Post processing submissions...'
submission_students = set()
for submission in project_submissions:
    submission['creation_date'] = parse_date(submission['creation_date'])
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['account_key'] = parse_int(submission['account_key'])
    submission['lesson_key'] = parse_int(submission['lesson_key'])
    submission_students.add(submission['account_key'])

print 'Enrolement - 1:'
print enrollments[0]
print 'Engagement - 1:'
print daily_engagement[0]
print 'Submission - 1:'
print project_submissions[0]


# Replace this with your code
enrollment_num_rows = len(enrollments)
enrollment_num_unique_students = len(
    enrollment_students)  # Replace this with your code

# Replace this with your code
engagement_num_rows = len(daily_engagement)
engagement_num_unique_students = len(
    engagement_students)  # Replace this with your code

# Replace this with your code
submission_num_rows = len(project_submissions)
submission_num_unique_students = len(
    submission_students)  # Replace this with your code

print 'No of enrollments:{0}'.format(enrollment_num_rows)
print 'No of engagements:{0}'.format(engagement_num_rows)
print 'No of submissions:{0}'.format(submission_num_rows)
print 'No of students enrolled: {0}'.format(enrollment_num_unique_students)
print 'No of students engaged: {0}'.format(engagement_num_unique_students)
print 'No of students submitted: {0}'.format(submission_num_unique_students)