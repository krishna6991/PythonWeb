from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Move

class MoveForm(ModelForm):
    class Meta:
        model = Move
        exclude = []

    def clean(self):
        x=self.cleaned_data.get("x")
        y=self.cleaned_data.get("y")
        game = self.instance.game
        try:
            if game.board()[y][x] is not None:
                raise ValidationError("square is not empty")
        except IndexError:
            raise ValidationError("Invalid coordinators")
        return self.cleaned_data
