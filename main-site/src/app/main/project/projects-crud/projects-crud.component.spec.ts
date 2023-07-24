import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProjectsCrudComponent } from './projects-crud.component';

describe('ProjectsCrudComponent', () => {
  let component: ProjectsCrudComponent;
  let fixture: ComponentFixture<ProjectsCrudComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProjectsCrudComponent]
    });
    fixture = TestBed.createComponent(ProjectsCrudComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
