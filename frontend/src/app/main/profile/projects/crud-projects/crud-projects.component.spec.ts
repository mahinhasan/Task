import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrudProjectsComponent } from './crud-projects.component';

describe('CrudProjectsComponent', () => {
  let component: CrudProjectsComponent;
  let fixture: ComponentFixture<CrudProjectsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CrudProjectsComponent]
    });
    fixture = TestBed.createComponent(CrudProjectsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
