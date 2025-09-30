describe('recorded test - login spec', () => {
  it('passes', () => {
    cy.visit('')
  })
});

it('record', function() {
  cy.visit('http://127.0.0.1:5500/index.html')
  cy.get('#optSignup a').click();
  cy.get('[name="email"]').click();
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('t');
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('test');
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('test@');
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('test@kea');
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('test@kea.');
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('test@kea.d');
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('test@kea.dk');
  cy.get('[name="password"]').click();
  cy.get('[name="password"]').clear();
  cy.get('[name="password"]').type('T');
  cy.get('[name="password"]').clear();
  cy.get('[name="password"]').type('Test');
  cy.get('[name="password"]').clear();
  cy.get('[name="password"]').type('Testing');
  cy.get('[name="repeatPassword"]').click();
  cy.get('[name="repeatPassword"]').clear();
  cy.get('[name="repeatPassword"]').type('T');
  cy.get('[name="repeatPassword"]').clear();
  cy.get('[name="repeatPassword"]').type('Testing');
  cy.get('#frmSignup [type="submit"]').click();
  cy.get('[href="login.html"]').click();
  cy.get('[name="email"]').click();
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('t');
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('test');
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('test@');
  cy.get('[name="email"]').clear();
  cy.get('[name="email"]').type('test@kea.dk');
  cy.get('[name="password"]').clear();
  cy.get('[name="password"]').type('T');
  cy.get('[name="password"]').clear();
  cy.get('[name="password"]').type('Testing');
  cy.get('#frmLogin [type="submit"]').click();
  
});