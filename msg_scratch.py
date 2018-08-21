count_msg = db.session.query(func.count(Messages.to_id==msg_for.user_id)).filter(Messages.to_id==msg_for.user_id, Messages.deleted_flag==False).scalar()
# counts number of valid msgs

count_msg = Messages.query.filter(Messages.to_id==msg_for.user_id,Messages.deleted_flag==False).all()
