import { ReactNode } from 'react';

import type { Metadata } from 'next';
import { Inter } from 'next/font/google';

import 'bootstrap/dist/css/bootstrap.min.css';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

const RootLayout = ({
  children,
}: Readonly<{
  children: ReactNode;
}>)  => (
  <html lang='en'>
    <body className={`p-12 ${inter.className}`}>{children}</body>
  </html>
);

export default RootLayout;
