

class AuthRouter():
    #     'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',
    # 'django.contrib.postgres',
    # 'rest_framework',
    # 'corsheaders',
    # 'accounts',
    # 'durin',
    # 'document_management',
    route_app_labels = {'admin', 'auth',
                        'contenttypes', 'sessions',
                        'messages', 'staticfiles',
                        'postgres', 'rest_framework',
                        'corsheaders', 'accounts',
                        'durin',
                        'document_management'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'dms'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'dms'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'dms'
        return None


class CrsRouter():
    route_app_labels = {'crs'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'crs'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'crs'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     """
    #     Make sure the auth and contenttypes apps only appear in the
    #     'auth_db' database.
    #     """
    #     if app_label in self.route_app_labels:
    #         return db == 'sikkimhc_pg'
    #     return None
