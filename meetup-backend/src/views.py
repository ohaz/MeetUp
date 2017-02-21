from application import application
from flask import render_template, jsonify, request
from models.group import Group
from models.user import User

@application.app.route('/')
def index():
    return 'HELLO WORLD'


# create new user
@application.app.route('/user/', methods=['POST'])
def user():
    # todo: create new User-ID
    print('create new user')
    d = {'userID': 'your new user id'}
    return jsonify(d)


# create new group -- or show list of all available groups
@application.app.route('/groups/', methods=['POST', 'GET'])
def groups():
    if request.method == 'POST':
        # todo: implement saving new group
        print('create new group')
        return ''
    else:
        # todo: get all available groups
        print('get all groups')
        list = [group.to_dict() for group in Group.query.all()]
        d = {'groups': list}
        return jsonify(d)


# join group
@application.app.route('/groups/<group_id>', methods=['POST'])
def join_group(group_id):
    # todo: implement joining
    print('join group')
    return ''


# list groupinfo & members of group
@application.app.route('/groups/<group_id>', methods=['GET'])
def group_info(group_id):
    # todo: get group info
    print('get group info')
    g = Group.query.filter(Group.uid == group_id).first()
    # d = {'group': group_id, 'name': 'tempname', 'members': ['Jonas', 'Richard', 'Simon']}
    return jsonify(g.all())


# leave group
@application.app.route('/groups/<group_id>/users/<user_id>', methods=['DELETE'])
def leave_group(group_id, user_id):
    # todo: leave a group
    print('leave group')
    return ''


# new call
@application.app.route('/groups/<group_id>/call/', methods=['POST'])
def call(group_id):
    # todo: implement calls
    print('new call')
    d = {'callID': 'random call id'}
    return jsonify(d)


# join call
@application.app.route('/groups/<group_id>/call/<call_id>', methods=['PUT'])
def join_call(group_id, call_id):
    # todo: implement join call
    print('join call')
    return ''


# subscribe or create Topic
@application.app.route('/groups/<group_id>/topics/<topic>', methods=['POST'])
def subscribe(group_id, topic):
    # todo: add user to topiclist
    print("subscribe to", topic)
    d = {'status': 'new / subscribed'}
    return jsonify(d)


# unsubscribe from Topic
@application.app.route('/groups/<group_id>/topics/<topic>', methods=['DELETE'])
def unsubscribe(group_id, topic):
    # todo: delete user from topiclist
    print("unsubscribe from", topic)
    d = {'status': 'unsubscribed'}
    return jsonify(d)


# list all topics
@application.app.route('/groups/<group_id>/topics/', methods=['GET'])
def list_topics(group_id):
    # todo: get all topics
    print('get all topics')
    d = {'topics': ['topic1', 'topic1>subtopic1']}
    return jsonify(d)




# For Admin webinterface
@application.app.route('/admin/groups/')
def admin_groups():
    return render_template('group-list.html', groups=['method park', 'uni'])
