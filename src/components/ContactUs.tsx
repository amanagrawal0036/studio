"use client";

import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";

export const ContactUs = () => {
  return (
    <Card>
      <CardHeader>
        <CardTitle>📞 Contact Us</CardTitle>
        <CardDescription>Get in touch with us for any queries or feedback.</CardDescription>
      </CardHeader>
      <CardContent>
        <p>
          Email: <a href="mailto:support@wicketwise.com">support@wicketwise.com</a>
        </p>
        <p>Phone: +1 (555) 123-4567</p>
        <p>Address: 123 Cricket Lane, Data City, USA</p>
      </CardContent>
    </Card>
  );
};
