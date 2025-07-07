from django import forms

class WorkoutForm(forms.Form):
    DIFFICULTY_CHOICES = [
        ('', '-- Выберите сложность --'),
        ('easy', 'Легкая'),
        ('hard', 'Тяжелая'),
    ]
    
    WORKOUT_TYPE_CHOICES = [
        ('', '-- Выберите вид нагрузки --'),
        ('cardio', 'Кардио'),
        ('strength', 'Силовая'),
    ]
    
    LOCATION_CHOICES = [
        ('', '-- Выберите место проведения --'),
        ('outdoor', 'Улица'),
        ('gym', 'Тренажёрный зал'),
    ]
    
    EXERCISE_CHOICES = [
        ('pushups', 'Отжимания от пола'),
        ('pullups', 'Подтягивания'),
        ('squats', 'Приседания'),
    ]
    
    EQUIPMENT_CHOICES = [
        ('belt', 'Пояс'),
        ('kettlebell', 'Гиря'),
        ('dumbbells', 'Гантели'),
        ('plates', 'Блины'),
    ]
    
    difficulty = forms.ChoiceField(
        choices=DIFFICULTY_CHOICES,
        required=True,
        label="Сложность"
    )
    workout_type = forms.ChoiceField(
        choices=WORKOUT_TYPE_CHOICES,
        required=True,
        label="Вид нагрузки"
    )
    location = forms.ChoiceField(
        choices=LOCATION_CHOICES,
        required=True,
        label="Место проведения"
    )
    equipment = forms.MultipleChoiceField(
        choices=EQUIPMENT_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Дополнительное оборудование"
    )
    exercise = forms.ChoiceField(
        choices=EXERCISE_CHOICES,
        required=True,
        label="Упражнение",
        initial='pushups'  # Устанавливаем отжимания по умолчанию как активное упражнение
    )
    reps_completed = forms.CharField(
        required=True,
        label="Выполнено повторов",
        help_text="Введите числа через пробел (например: 5 10 15 25)"
    )