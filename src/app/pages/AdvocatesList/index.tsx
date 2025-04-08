import { SyntheticEvent, useEffect, useState } from "react";

import Page from './Page';
import { AdvocateType } from './types';

const AdvocatesList = () => {
  const [advocates, setAdvocates] = useState<Array<AdvocateType>>([]);
  // TODO: Issue #5 use debounce
  const [filteredAdvocates, setFilteredAdvocates] = useState<Array<AdvocateType>>([]);

  useEffect(() => {
    fetch("/api/advocates").then((response) => {
      response.json().then((jsonResponse) => {
        setAdvocates(jsonResponse.data);
        setFilteredAdvocates(jsonResponse.data);
      });
    });
  }, []);

  const onChange = (e: SyntheticEvent) => {
    const searchTerm = e.target.value;

    // TODO: Issue #6 apply mature searching
    const filteredAdvocates = advocates.filter((advocate) => {
      return (
        advocate.firstName.includes(searchTerm) ||
        advocate.lastName.includes(searchTerm) ||
        advocate.city.includes(searchTerm) ||
        advocate.degree.includes(searchTerm) ||
        advocate.specialties.join(', ').includes(searchTerm) ||
        `${advocate.phoneNumber}`.includes(searchTerm)
      );
    });

    setFilteredAdvocates(filteredAdvocates);
  };

  const onClick = () => {
    setFilteredAdvocates(advocates);
  };

  return <Page advocates={filteredAdvocates} onSearch={onChange} onReset={onClick}/>
};

export default AdvocatesList;
