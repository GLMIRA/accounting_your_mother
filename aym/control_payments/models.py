import uuid
from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)
from django.contrib.auth.models import User

from . import validators as custom_validators


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="User",
        help_text="User of the user profile",
        null=False,
        blank=False,
        db_column="user",
        db_comment="User of the user profile",
        on_delete=models.CASCADE,
        error_messages={
            "blank": "User cannot be blank",
            "null": "User cannot be null",
        },
    )
    cpf = models.CharField(
        verbose_name="CPF",
        help_text="CPF of the user",
        max_length=11,
        null=False,
        blank=False,
        unique=True,
        db_column="cpf",
        db_comment="CPF of the user",
        validators=[custom_validators.validate_cpf],
        error_messages={
            "blank": "CPF cannot be blank",
            "null": "CPF cannot be null",
            "max_length": "CPF cannot be longer than 11 characters",
        },
    )
    birth_date = models.DateField(
        verbose_name="Birth date",
        help_text="Birth date of the user",
        null=False,
        blank=False,
        db_column="birth_date",
        db_comment="Birth date of the user",
        validators=[custom_validators.validate_birth_date],
        error_messages={
            "blank": "Birth date cannot be blank",
            "null": "Birth date cannot be null",
        },
    )
    discord_nickname = models.CharField(
        verbose_name="Discord nickname",
        help_text="Discord nickname of the user",
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        db_column="discord_nickname",
        db_comment="Discord nickname of the user",
        validators=[
            MinLengthValidator(
                3, message="Discord nickname must have at least 3 characters"
            ),
            RegexValidator(
                regex=r"^[a-zA-Z0-9_]+$",
                message="Discord nickname must have only letters, numbers and underscores",
            ),
        ],
        error_messages={
            "blank": "Discord nickname cannot be blank",
            "null": "Discord nickname cannot be null",
            "max_length": "Discord nickname cannot be longer than 255 characters",
        },
    )
    active = models.BooleanField(
        verbose_name="Active",
        help_text="Active of the user",
        null=False,
        blank=False,
        db_column="active",
        db_comment="Active of the user",
        default=True,
        error_messages={
            "blank": "Active cannot be blank",
            "null": "Active cannot be null",
        },
    )

    class Meta:
        db_table = "user_profile"
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"

    def __str__(self):
        return f"{self.__class__}:{self.cpf} - {self.user}"


class DebtType(models.Model):
    id = models.UUIDField(
        primary_key=True,
        verbose_name="ID",
        help_text="ID of the debt type",
        null=False,
        blank=False,
        default=uuid.uuid4,
        editable=False,
        db_column="id",
        db_comment="ID of the debt type",
        error_messages={
            "blank": "ID cannot be blank",
            "null": "ID cannot be null",
        },
    )
    name = models.CharField(
        verbose_name="Name",
        help_text="Name of the debt type",
        max_length=30,
        null=False,
        blank=False,
        db_column="name",
        db_comment="Name of the debt type",
        validators=[
            MinLengthValidator(3, message="Name must have at least 10 characters"),
        ],
        error_messages={
            "blank": "Name cannot be blank",
            "null": "Name cannot be null",
            "max_length": "Name cannot be longer than 30 characters",
        },
    )
    description = models.CharField(
        verbose_name="Description",
        help_text="Description of the debt type",
        max_length=255,
        null=False,
        blank=False,
        db_column="description",
        db_comment="Description of the debt type",
        validators=[
            MinLengthValidator(
                10, message="Description must have at least 10 characters"
            ),
        ],
        error_messages={
            "blank": "Description cannot be blank",
            "null": "Description cannot be null",
            "max_length": "Description cannot be longer than 255 characters",
        },
    )
    active = models.BooleanField(
        verbose_name="Active",
        help_text="Active of the debt type",
        null=False,
        blank=False,
        db_column="active",
        db_comment="Active of the debt type",
        default=True,
        error_messages={
            "blank": "Active cannot be blank",
            "null": "Active cannot be null",
        },
    )

    class Meta:
        db_table = "debt_type"
        verbose_name = "Debt type"
        verbose_name_plural = "Debt types"

    def __str__(self):
        return f"{self.__class__}:{self.id} - {self.name}"


class ApportionmentRules(models.Model):
    id = models.UUIDField(
        primary_key=True,
        verbose_name="ID",
        help_text="ID of the apportionment rule",
        null=False,
        blank=False,
        default=uuid.uuid4,
        editable=False,
        db_column="id",
        db_comment="ID of the apportionment rule",
        error_messages={
            "blank": "ID cannot be blank",
            "null": "ID cannot be null",
        },
    )
    debt_type = models.ForeignKey(
        DebtType,
        verbose_name="Debt type",
        help_text="Debt type of the apportionment rule",
        null=False,
        blank=False,
        db_column="debt_type",
        db_comment="Debt type of the apportionment rule",
        on_delete=models.CASCADE,
        error_messages={
            "blank": "Debt type cannot be blank",
            "null": "Debt type cannot be null",
        },
    )
    user = models.ForeignKey(
        User,
        verbose_name="User",
        help_text="User of the apportionment rule",
        null=False,
        blank=False,
        db_column="user",
        db_comment="user of the apportionment rule",
        on_delete=models.CASCADE,
        error_messages={
            "blank": "User cannot be blank",
            "null": "User cannot be null",
        },
    )
    percentage = models.DecimalField(
        verbose_name="Percentage",
        help_text="Percentage of the apportionment rule",
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        db_column="percentage",
        db_comment="Percentage of the apportionment rule",
        validators=[
            MinValueValidator(0.01, message="Percentage must be at least 0.01"),
            MaxValueValidator(100.00, message="Percentage must be at most 100.00"),
        ],
        error_messages={
            "blank": "Percentage cannot be blank",
            "null": "Percentage cannot be null",
            "max_digits": "Percentage cannot have more than 5 digits",
            "max_decimal_places": "Percentage cannot have more than 2 decimal places",
        },
    )
    active = models.BooleanField(
        verbose_name="Active",
        help_text="Active of the apportionment rule",
        null=False,
        blank=False,
        db_column="active",
        db_comment="Active of the apportionment rule",
        default=True,
        error_messages={
            "blank": "Active cannot be blank",
            "null": "Active cannot be null",
        },
    )

    class Meta:
        db_table = "apportionment_rules"
        verbose_name = "Apportionment rule"
        verbose_name_plural = "Apportionment rules"

    def __str__(self):
        return f"{self.__class__}:{self.id} - {self.debt_type} - {self.user}"


class Debts(models.Model):
    id = models.UUIDField(
        primary_key=True,
        verbose_name="ID",
        help_text="ID of the debt",
        null=False,
        blank=False,
        default=uuid.uuid4,
        editable=False,
        db_column="id",
        db_comment="ID of the debt",
        error_messages={
            "blank": "ID cannot be blank",
            "null": "ID cannot be null",
        },
    )
    due_date = models.DateField(
        verbose_name="Due date",
        help_text="Due date of the debt",
        null=False,
        blank=False,
        db_column="due_date",
        db_comment="Due date of the debt",
        error_messages={
            "blank": "Due date cannot be blank",
            "null": "Due date cannot be null",
        },
    )
    debt_value = models.DecimalField(
        verbose_name="Debt value",
        help_text="Debt value of the debt",
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        db_column="debt_value",
        db_comment="Debt value of the debt",
        validators=[
            MinValueValidator(0.01, message="Debt value must be at least 0.01"),
            MaxValueValidator(
                999999.99, message="Debt value must be at most 999999.99"
            ),
        ],
        error_messages={
            "blank": "Debt value cannot be blank",
            "null": "Debt value cannot be null",
            "max_digits": "Debt value cannot have more than 10 digits",
            "max_decimal_places": "Debt value cannot have more than 2 decimal places",
        },
    )
    debt_type = models.ForeignKey(
        DebtType,
        verbose_name="Debt type",
        help_text="Debt type of the debt",
        null=False,
        blank=False,
        db_column="debt_type",
        db_comment="Debt type of the debt",
        on_delete=models.CASCADE,
        error_messages={
            "blank": "Debt type cannot be blank",
            "null": "Debt type cannot be null",
        },
    )
    active = models.BooleanField(
        verbose_name="Active",
        help_text="Active of the debt",
        null=False,
        blank=False,
        db_column="active",
        db_comment="Active of the debt",
        default=True,
        error_messages={
            "blank": "Active cannot be blank",
            "null": "Active cannot be null",
        },
    )

    class Meta:
        db_table = "debt"
        verbose_name = "Debt"
        verbose_name_plural = "Debts"

    def __str__(self):
        return f"{self.__class__}:{self.id} - {self.debt_type}"


class Apportionment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        verbose_name="ID",
        help_text="ID of the apportionment",
        null=False,
        blank=False,
        default=uuid.uuid4,
        editable=False,
        db_column="id",
        db_comment="ID of the apportionment",
        error_messages={
            "blank": "ID cannot be blank",
            "null": "ID cannot be null",
        },
    )
    debt = models.ForeignKey(
        Debts,
        verbose_name="Debt",
        help_text="Debt of the apportionment",
        null=False,
        blank=False,
        db_column="debt",
        db_comment="Debt of the apportionment",
        on_delete=models.CASCADE,
        error_messages={
            "blank": "Debt cannot be blank",
            "null": "Debt cannot be null",
        },
    )
    user = models.ForeignKey(
        User,
        verbose_name="User",
        help_text="User of the apportionment",
        null=False,
        blank=False,
        db_column="user",
        db_comment="User of the apportionment",
        on_delete=models.CASCADE,
        error_messages={
            "blank": "User cannot be blank",
            "null": "User cannot be null",
        },
    )
    value = models.DecimalField(
        verbose_name="Value",
        help_text="Value of the apportionment",
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        db_column="value",
        db_comment="Value of the apportionment",
        validators=[
            MinValueValidator(0.01, message="Value must be at least 0.01"),
            MaxValueValidator(999999.99, message="Value must be at most 999999.99"),
        ],
        error_messages={
            "blank": "Value cannot be blank",
            "null": "Value cannot be null",
            "max_digits": "Value cannot have more than 10 digits",
            "max_decimal_places": "Value cannot have more than 2 decimal places",
        },
    )
    active = models.BooleanField(
        verbose_name="Active",
        help_text="Active of the apportionment",
        null=False,
        blank=False,
        db_column="active",
        db_comment="Active of the apportionment",
        default=True,
        error_messages={
            "blank": "Active cannot be blank",
            "null": "Active cannot be null",
        },
    )

    class Meta:
        db_table = "apportionment"
        verbose_name = "Apportionment"
        verbose_name_plural = "Apportionments"

    def __str__(self):
        return f"{self.__class__}:{self.id} - {self.debt} - {self.user}"


class Payment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        verbose_name="ID",
        help_text="ID of the payment",
        null=False,
        blank=False,
        default=uuid.uuid4,
        editable=False,
        db_column="id",
        db_comment="ID of the payment",
        error_messages={
            "blank": "ID cannot be blank",
            "null": "ID cannot be null",
        },
    )
    user = models.ForeignKey(
        User,
        verbose_name="User",
        help_text="User of the payment",
        null=False,
        blank=False,
        db_column="user",
        db_comment="User of the payment",
        on_delete=models.CASCADE,
        error_messages={
            "blank": "User cannot be blank",
            "null": "User cannot be null",
        },
    )
    pay_date = models.DateField(
        verbose_name="Pay date",
        help_text="Pay date of the payment",
        null=False,
        blank=False,
        db_column="pay_date",
        db_comment="Pay date of the payment",
        error_messages={
            "blank": "Pay date cannot be blank",
            "null": "Pay date cannot be null",
        },
    )
    pay_value = models.DecimalField(
        verbose_name="Pay value",
        help_text="Pay value of the payment",
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        db_column="pay_value",
        db_comment="Pay value of the payment",
        validators=[
            MinValueValidator(0.01, message="Pay value must be at least 0.01"),
            MaxValueValidator(999999.99, message="Pay value must be at most 999999.99"),
        ],
        error_messages={
            "blank": "Pay value cannot be blank",
            "null": "Pay value cannot be null",
            "max_digits": "Pay value cannot have more than 10 digits",
            "max_decimal_places": "Pay value cannot have more than 2 decimal places",
        },
    )

    class Meta:
        db_table = "payment"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"{self.__class__}:{self.id} - {self.user}"


class DebtCollection(models.Model):
    id = models.UUIDField(
        primary_key=True,
        verbose_name="ID",
        help_text="ID of the debt collection",
        null=False,
        blank=False,
        default=uuid.uuid4,
        editable=False,
        db_column="id",
        db_comment="ID of the debt collection",
        error_messages={
            "blank": "ID cannot be blank",
            "null": "ID cannot be null",
        },
    )
    user = models.ForeignKey(
        User,
        verbose_name="User",
        help_text="User of the debt collection",
        null=False,
        blank=False,
        db_column="user",
        db_comment="User of the debt collection",
        on_delete=models.CASCADE,
        error_messages={
            "blank": "User cannot be blank",
            "null": "User cannot be null",
        },
    )
    debt_collection_date = models.DateField(
        verbose_name="Debt collection date",
        help_text="Debt collection date of the debt collection",
        null=False,
        blank=False,
        db_column="debt_collection_date",
        db_comment="Debt collection date of the debt collection",
        error_messages={
            "blank": "Debt collection date cannot be blank",
            "null": "Debt collection date cannot be null",
        },
    )
    debt_collection_value = models.DecimalField(
        verbose_name="Debt collection value",
        help_text="Debt collection value of the debt collection",
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        db_column="debt_collection_value",
        db_comment="Debt collection value of the debt collection",
        validators=[
            MinValueValidator(
                0.01, message="Debt collection value must be at least 0.01"
            ),
            MaxValueValidator(
                999999.99, message="Debt collection value must be at most 999999.99"
            ),
        ],
        error_messages={
            "blank": "Debt collection value cannot be blank",
            "null": "Debt collection value cannot be null",
            "max_digits": "Debt collection value cannot have more than 10 digits",
            "max_decimal_places": "Debt collection value cannot have more than 2 decimal places",
        },
    )

    class Meta:
        db_table = "debt_collection"
        verbose_name = "Debt collection"
        verbose_name_plural = "Debt collections"

    def __str__(self):
        return f"{self.__class__}:{self.id} - {self.user}"
