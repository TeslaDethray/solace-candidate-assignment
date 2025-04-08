import { SyntheticEvent } from 'react';

import { Stack } from 'react-bootstrap';

import Search from './Search';
import Table from './Table';
import AdvocateType from './types';

const AdvocateList = (
  {
    advocates,
    onReset,
    onSearch,
  }:
  {
    advocates: Array<AdvocateType>;
    onReset?: () => void;
    onSearch?: (_: SyntheticEvent) => void;
  }
) => (
  <Stack gap={3}>
    <h1 className="h1">Solace Advocates</h1>
    <Search onReset={onReset} onSearch={onSearch} />
    <Table advocates={advocates} />
  </Stack>
);

export default AdvocateList;
