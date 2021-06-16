from app.schema.inputs import Input


class Rules:

    def evalue(self, input: Input):
        if input.first_number == 1.0:
            return "BIEN"
        else:
            return "MAL"