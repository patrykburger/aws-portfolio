import boto3

# Tworzymy klienta do obsługi usługi EC2
ec2 = boto3.client('ec2')

try:
    # Wysyłamy zapytanie API do AWS o listę instancji
    response = ec2.describe_instances()
    print("Połączenie z AWS zrealizowane pomyślnie!")
    print(f"Liczba rezerwacji EC2: {len(response['Reservations'])}")
except Exception as e:
    print(f"Błąd podczas połączenia z AWS: {e}")

import boto3

# Tworzymy klienta dla usługi STS (Security Token Service)
sts_client = boto3.client('sts')

# Pobieramy informacje o zalogowanej tożsamości
identity = sts_client.get_caller_identity()

print("--- DETALE TWOJEGO KONTA AWS ---")
print(f"Account ID: {identity['Account']}")
print(f"User ARN:   {identity['Arn']}")
print(f"User ID:    {identity['UserId']}")