import { SyntheticEvent } from 'react';

import { Button, FormControl, FormLabel, Stack } from 'react-bootstrap';

const SEARCH_INPUT_NAME = 'advocate_search_string';

const PaddedDiv = (props) => (<div className="p-1" {...props} />);

const Search = (
  {
    onReset = () => {},
    onSearch = (_: SyntheticEvent) => {},
  }:
  {
    onReset?: () => void;
    onSearch?: (_: SyntheticEvent) => void;
  }
) => (
  <Stack direction="horizontal" gap={3}>
    <PaddedDiv className="p-1">
      <FormLabel htmlFor={SEARCH_INPUT_NAME}>Search:</FormLabel>
    </PaddedDiv>
    <PaddedDiv className="p-1">
      <FormControl name={SEARCH_INPUT_NAME} onChange={onSearch} rows={1} type="textarea" />
    </PaddedDiv>
    <PaddedDiv className="p-1">
      <Button onClick={onReset}>Reset Search</Button>
    </PaddedDiv>
  </Stack>
);

export default Search;
