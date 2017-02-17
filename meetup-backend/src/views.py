from application import application
from flask import render_template, jsonify, request


@application.app.route('/')
def index():
    return 'HELLO WORLD'

# create new user
@application.app.route('/user/', methods=['POST'])
def user():
    # todo: create new User-ID
    d = {'userID': 'your new user id'}
    return jsonify(d)

# create new group -- or show list of all available groups
@application.app.route('/groups/', methods=['POST', 'GET'])
def groups():
    if request.method == 'POST':
        # todo: implement saving new group
        print('try to create new group')
        return ''
    else:
        d = {'groups':['mp','uni','richards fun club']}
        return jsonify(d)

# join group
@application.app.route('/groups/<group_id>', methods=['POST'])
def join_group(group_id):
# todo: implement joining
        return ''

# list groupinfo & members of group
@application.app.route('/groups/<group_id>', methods=['GET'])
def group_info(group_id):
    d = {'group': group_id, 'name': 'tempname', 'members': ['Jonas', 'Richard', 'Simon']}
    return jsonify(d)

# leave group
@application.app.route('/groups/<group_id>/users/<user_id>', methods=['DELETE'])
def leave_group(group_id, user_id):
    # todo: leave a group
    return ''

# new call
@application.app.route('/groups/<group_id>/call/', methods=['POST'])
def call(group_id):
    # todo: implement calls
    d = {'callID': 'random call id'}
    return jsonify(d)

# join call
@application.app.route('/groups/<group_id>/call/<call_id>', methods=['PUT'])
def join_call(group_id, call_id):
    # todo: implement join call
    return ''

# subscribe or create Topic
@application.app.route('/groups/<group_id>/topics/<topic>', methods=['POST'])
def subscribe(group_id, topic):
    print("subscribe to", topic)
    d = {'status': 'new / subscribed'}
    return jsonify(d)

# unsubscribe from Topic
@application.app.route('/groups/<group_id>/topics/<topic>', methods=['DELETE'])
def unsubscribe(group_id, topic):
    print("unsubscribe from", topic)
    d = {'status': 'unsubscribed'}
    return jsonify(d)

# list all topics
@application.app.route('/groups/<group_id>/topics/', methods=['GET'])
def list_topics(group_id):
    # todo:
    d = {'topics': ['topic1', 'topic1>subtopic1']}
    return jsonify(d)




# For Admin webinterface
@application.app.route('/admin/groups/')
def admin_groups():
    return render_template('group-list.html', groups=['method park', 'uni'])
