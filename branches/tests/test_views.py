from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from branches.models import Branch


class ViewBranchesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Branch.objects.create(
            branch_name='Yummy Food Restaurant - IOI City Mall',
            branch_address='LG-239, Lower Ground Floor, IOI City Mall, Lebuh IRC, IOI Resort City, 62502 Putrajaya',
            branch_contact='+60 3-4258 8889',
            created_at=timezone.now()
        )
        Branch.objects.create(
            branch_name='Yummy Food Restaurant - IOI City Mall',
            branch_address='LG-239, Lower Ground Floor, IOI City Mall, Lebuh IRC, IOI Resort City, 62502 Putrajaya',
            branch_contact='+60 3-4258 8889',
            created_at=timezone.now()
        )

    def test_view_branches_view(self):
        response = self.client.get(reverse('branches:branch'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'branches.html')
        self.assertEqual(len(response.context['all_branches']), 2)
