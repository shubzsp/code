from django.db import models


class DbRouter:
    """
    A router to control all database operations on models in the
    user application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to users_db.
        """
        if model._meta.app_label == 'product':
            return 'product_db'
        
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to product_db.
        """
        if model._meta.app_label == 'product':
            return 'product_db'
        
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'product' or \
           obj2._meta.app_label == 'product':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'product_db'
        database.
        """
        if app_label == 'product':
            return db == 'product_db'
        return None


class Product_model(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    updated_at=models.TimeField( auto_now=True)
    weight=models.CharField(max_length=100)
    created_at=models.TimeField(auto_now_add=True)
    
    class Meta:
        app_label='product'