from rest_framework import serializers
from .models import Machine, TO, Claim


class MachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Machine
        fields = (
            'id', 'n_machine', 'type_machine', 'n_motor', 'type_motor', 'n_tranc',
            'type_tranc', 'n_vmost', 'type_vmost', 'n_cmost', 'type_cmost', 'order',
            'buyer', 'address', 'options', 'client', 'company')


class TOSerializer(serializers.ModelSerializer):

    class Meta:
        model = TO
        fields = ('id', 'type_to', 'date', 'narabotka', 'order', 'date_order', 'doTOservice', 'machine')


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = (
                'id', 'date', 'narabotka', 'detail', 'info', 'fix', 'fix_detail', 'fix_date',
                'stop_date', 'machine', 'service')