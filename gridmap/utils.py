__author__ = 'glazek'


def get_scheduler_type(session=None):
    scheduler_type_dict = {
        'GE': 'SGE',
        'OSG/GE': 'SGE',
        'SGE': 'SGE',
        'SLURM': 'SLURM'
    }
    if session:
        return scheduler_type_dict.get(session.drmsInfo.split()[0])
    try:
        from drmaa import Session
        cluster_type = Session.drmsInfo.split()[0]
        return scheduler_type_dict.get(cluster_type)
    except (ImportError, RuntimeError, OSError):
        return None